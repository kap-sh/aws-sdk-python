
import pytest
from aws_sdk_mpa._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_mpa._rule_engine._endpoint_runtime import EndpointError
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
    assert result.url == 'https://mpa-fips.us-east-1.api.aws'


def test_4_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-east-1',
        UseFIPS=False,
    )

    result = resolve(params)
    assert result.url == 'https://mpa.us-east-1.api.aws'


def test_5_for_region_cn_northwest_1_with_fips_enab():
    """For region cn-northwest-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='cn-northwest-1',
        UseFIPS=True,
    )

    result = resolve(params)
    assert result.url == 'https://mpa-fips.cn-northwest-1.api.amazonwebservices.com.cn'


def test_6_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='cn-northwest-1',
        UseFIPS=False,
    )

    result = resolve(params)
    assert result.url == 'https://mpa.cn-northwest-1.api.amazonwebservices.com.cn'


def test_7_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-gov-west-1',
        UseFIPS=True,
    )

    result = resolve(params)
    assert result.url == 'https://mpa-fips.us-gov-west-1.api.aws'


def test_8_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(
        Region='us-gov-west-1',
        UseFIPS=False,
    )

    result = resolve(params)
    assert result.url == 'https://mpa.us-gov-west-1.api.aws'


def test_9_missing_region():
    """Missing region"""
    params = EndpointParams(
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)


