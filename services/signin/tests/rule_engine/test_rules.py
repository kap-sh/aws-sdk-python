import pytest
from aws_sdk_signin._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_signin._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_control_plane_operation_in_us_east_1__aw():
    """Control Plane operation in us-east-1 (aws partition)"""
    params = EndpointParams(IsControlPlane=True, Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://signin.us-east-1.api.aws'

def test_control_plane_operation_in_cn_north_1__a():
    """Control Plane operation in cn-north-1 (aws-cn partition)"""
    params = EndpointParams(IsControlPlane=True, Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://signin.cn-north-1.api.amazonwebservices.com.cn'

def test_data_plane_operation_in_us_east_1():
    """Data Plane operation in us-east-1"""
    params = EndpointParams(IsControlPlane=False, Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://us-east-1.signin.aws.amazon.com'

def test_data_plane_operation_in_us_east_1__iscon():
    """Data Plane operation in us-east-1 (IsControlPlane not set)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://us-east-1.signin.aws.amazon.com'

def test_data_plane_operation_in_cn_north_1():
    """Data Plane operation in cn-north-1"""
    params = EndpointParams(IsControlPlane=False, Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://cn-north-1.signin.amazonaws.cn'

def test_data_plane_operation_in_us_gov_west_1():
    """Data Plane operation in us-gov-west-1"""
    params = EndpointParams(IsControlPlane=False, Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://us-gov-west-1.signin.amazonaws-us-gov.com'

def test_fips_endpoint_in_us_gov_west_1__global_e():
    """FIPS endpoint in us-gov-west-1 (global endpoint)"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://signin-fips.amazonaws-us-gov.com'

def test_fips_endpoint_in_us_gov_east_1__regional():
    """FIPS endpoint in us-gov-east-1 (regional endpoint)"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://us-gov-east-1.signin-fips.amazonaws-us-gov.com'

def test_fips_endpoint_in_us_east_1():
    """FIPS endpoint in us-east-1"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://signin-fips.us-east-1.amazonaws.com'

def test_dualstack_falls_through_to_default_sdk_e():
    """DualStack falls through to default SDK endpoint in us-east-1 (aws partition)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://signin.us-east-1.api.aws'

def test_dualstack_falls_through_to_default_sdk_e():
    """DualStack falls through to default SDK endpoint in cn-north-1 (aws-cn partition)"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://signin.cn-north-1.api.amazonwebservices.com.cn'

def test_dualstack_falls_through_to_default_sdk_e():
    """DualStack falls through to default SDK endpoint in us-gov-west-1 (aws-us-gov partition)"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://signin.us-gov-west-1.api.aws'

def test_custom_sdk_endpoint_override():
    """Custom SDK endpoint override"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://custom.signin.example.com', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://custom.signin.example.com'

def test_iso_partition__us_iso_east_1_():
    """ISO partition (us-iso-east-1)"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://us-iso-east-1.signin.c2shome.ic.gov'

def test_iso_b_partition__us_isob_east_1_():
    """ISO-B partition (us-isob-east-1)"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://us-isob-east-1.signin.sc2shome.sgov.gov'