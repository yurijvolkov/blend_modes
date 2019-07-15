import cv2
import pytest

from blend_modes import *

_TEST_LIMIT = 10  # test fails if max. image color difference is > test_limit
_TEST_TOLERANCE = 0.001  # max. ratio of RGBA pixels that may not match test criteria

def _test_criteria(out, comp):
    return (np.sum(np.absolute(out - comp) > _TEST_LIMIT)) / np.prod(comp.shape) < _TEST_TOLERANCE

@pytest.fixture
def img_in():
    return cv2.imread('./orig.png', -1).astype(float)

@pytest.fixture
def img_layer():
    return cv2.imread('./layer.png', -1).astype(float)


@pytest.fixture
def img_layer_50p():
    return cv2.imread('./layer_50p.png', -1).astype(float)


def test_addition(img_in, img_layer):
    out = soft_light(img_in, img_layer, 0.5)
    comp = cv2.imread('./soft_light.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_darken_only(img_in, img_layer):
    out = darken_only(img_in, img_layer, 0.5)
    comp = cv2.imread('./darken_only.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_multiply(img_in, img_layer):
    out = multiply(img_in, img_layer, 0.5)
    comp = cv2.imread('./multiply.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_difference(img_in, img_layer):
    out = difference(img_in, img_layer, 0.5)
    comp = cv2.imread('./difference.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_divide(img_in, img_layer):
    out = divide(img_in, img_layer, 0.5)
    comp = cv2.imread('./divide.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_dodge(img_in, img_layer):
    out = dodge(img_in, img_layer, 0.5)
    comp = cv2.imread('./dodge.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_grain_extract(img_in, img_layer):
    out = grain_extract(img_in, img_layer, 0.5)
    comp = cv2.imread('./grain_extract.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_grain_merge(img_in, img_layer):
    out = grain_merge(img_in, img_layer, 0.5)
    comp = cv2.imread('./grain_merge.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_hard_light(img_in, img_layer):
    out = hard_light(img_in, img_layer, 0.5)
    comp = cv2.imread('./hard_light.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_lighten_only(img_in, img_layer):
    out = lighten_only(img_in, img_layer, 0.5)
    comp = cv2.imread('./lighten_only.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_soft_light_50p(img_in, img_layer_50p):
    out = soft_light(img_in, img_layer_50p, 0.8)
    comp = cv2.imread('./soft_light_50p.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_overlay(img_in, img_layer):
    out = overlay(img_in, img_layer, 0.5)
    comp = cv2.imread('./overlay.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_normal_50p(img_in, img_layer):
    out = normal(img_in, img_layer, 0.5)
    comp = cv2.imread('./normal_50p.png', -1).astype(float)
    assert _test_criteria(out, comp)


def test_normal_100p(img_in, img_layer):
    out = normal(img_in, img_layer, 1.0)
    comp = cv2.imread('./normal_100p.png', -1).astype(float)
    assert _test_criteria(out, comp)
