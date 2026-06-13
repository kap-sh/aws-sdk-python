
import pytest
from aws_sdk_arc_region_switch._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_arc_region_switch._rule_engine._endpoint_runtime import EndpointError
import re
import zapros


def test_1_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled"""
    params = EndpointParams(
        Endpoint='https://example.com',
        UseFIPS=False,
    )

    result = resolve(params)
    assert result.url == 'https://example.com'


def test_2_for_custom_endpoint_with_fips_enabled():
    """For custom endpoint with fips enabled"""
    params = EndpointParams(
        Endpoint='https://example.com',
        UseFIPS=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)


def test_3_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-fips.us-east-1.api.aws'


def test_4_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=False,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch.us-east-1.api.aws'


def test_5_for_region_cn_northwest_1_with_fips_enab():
    """For region cn-northwest-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='cn-northwest-1',
        UseFIPS=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-fips.cn-northwest-1.api.amazonwebservices.com.cn'


def test_6_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='cn-northwest-1',
        UseFIPS=False,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch.cn-northwest-1.api.amazonwebservices.com.cn'


def test_7_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-gov-west-1',
        UseFIPS=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-fips.us-gov-west-1.api.aws'


def test_8_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-gov-west-1',
        UseFIPS=False,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch.us-gov-west-1.api.aws'


def test_9_missing_region():
    """Missing region"""
    params = EndpointParams(
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)


def test_10_control_plane_operation_with_dualstack_i():
    """Control plane operation with DualStack in us-west-2 routes to us-east-1 DualStack endpoint"""
    params = EndpointParams(
        Region='us-west-2',
        UseControlPlaneEndpoint=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane.us-east-1.api.aws'


def test_11_control_plane_operation_with_endpoint_se():
    """Control plane operation with endpoint set in us-east-1 routes to provided endpoint"""
    params = EndpointParams(
        Region='us-east-1',
        UseControlPlaneEndpoint=True,
        Endpoint='https://amazonaws.com',
    )

    result = resolve(params)
    assert result.url == 'https://amazonaws.com'


def test_12_control_plane_operation_with_endpoint_se():
    """Control plane operation with endpoint set in us-west-2 routes to provided endpoint"""
    params = EndpointParams(
        Region='us-west-2',
        UseControlPlaneEndpoint=True,
        Endpoint='https://amazonaws.com',
    )

    result = resolve(params)
    assert result.url == 'https://amazonaws.com'


def test_13_control_plane_operation_in_us_west_2__st():
    """Control plane operation in us-west-2 (standard partition) routes to us-east-1"""
    params = EndpointParams(
        Region='us-west-2',
        UseControlPlaneEndpoint=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane.us-east-1.api.aws'


def test_14_control_plane_operation_in_cn_north_1__c():
    """Control plane operation in cn-north-1 (China partition) routes to cn-north-1 with China DNS suffix"""
    params = EndpointParams(
        Region='cn-north-1',
        UseControlPlaneEndpoint=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane.cn-north-1.api.amazonwebservices.com.cn'


def test_15_control_plane_operation_in_cn_northwest_():
    """Control plane operation in cn-northwest-1 (China partition) routes to cn-north-1 with China DNS suffix"""
    params = EndpointParams(
        Region='cn-northwest-1',
        UseControlPlaneEndpoint=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane.cn-north-1.api.amazonwebservices.com.cn'


def test_16_control_plane_operation_in_us_gov_west_1():
    """Control plane operation in us-gov-west-1 (GovCloud partition) routes to us-gov-west-1 with GovCloud DNS suffix"""
    params = EndpointParams(
        Region='us-gov-west-1',
        UseControlPlaneEndpoint=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane.us-gov-west-1.api.aws'


def test_17_control_plane_operation_in_us_gov_east_1():
    """Control plane operation in us-gov-east-1 (GovCloud partition) routes to us-gov-west-1 with GovCloud DNS suffix"""
    params = EndpointParams(
        Region='us-gov-east-1',
        UseControlPlaneEndpoint=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane.us-gov-west-1.api.aws'


def test_18_control_plane_operation_with_fips_in_us_():
    """Control plane operation with FIPS in us-west-2 routes to us-east-1 FIPS endpoint"""
    params = EndpointParams(
        Region='us-west-2',
        UseControlPlaneEndpoint=True,
        UseFIPS=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane-fips.us-east-1.api.aws'


def test_19_control_plane_operation_with_fips_in_us_():
    """Control plane operation with FIPS in us-east-1 routes to us-east-1 FIPS endpoint"""
    params = EndpointParams(
        Region='us-east-1',
        UseControlPlaneEndpoint=True,
        UseFIPS=True,
    )

    result = resolve(params)
    assert result.url == 'https://arc-region-switch-control-plane-fips.us-east-1.api.aws'


def test_20_control_plane_operation_with_fips_in_cn_():
    """Control plane operation with FIPS in CN returns an error"""
    params = EndpointParams(
        Region='cn-north-1',
        UseControlPlaneEndpoint=True,
        UseFIPS=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported in this partition')):
        resolve(params)


def test_21_control_plane_operation_with_endpoint_se():
    """Control plane operation with endpoint set using FIPS in us-east-1 errors"""
    params = EndpointParams(
        Region='us-east-1',
        UseControlPlaneEndpoint=True,
        UseFIPS=True,
        Endpoint='https://amazonaws.com',
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)


def test_22_control_plane_operation_with_endpoint_se():
    """Control plane operation with endpoint set using FIPS in us-west-2 routes to provided endpoint"""
    params = EndpointParams(
        Region='us-west-2',
        UseControlPlaneEndpoint=True,
        UseFIPS=True,
        Endpoint='https://amazonaws.com',
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)


