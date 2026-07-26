import pytest
from capo_codecatalyst._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codecatalyst._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_override_endpoint():
    """Override endpoint"""
    params = EndpointParams(Endpoint='https://test.codecatalyst.global.api.aws')
    result = resolve(params)
    assert result.url == 'https://test.codecatalyst.global.api.aws'

def test_default_endpoint__region_not_set_():
    """Default endpoint (region not set)"""
    params = EndpointParams()
    result = resolve(params)
    assert result.url == 'https://codecatalyst.global.api.aws'

def test_default_fips_endpoint__region_not_set_():
    """Default FIPS endpoint (region not set)"""
    params = EndpointParams(UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://codecatalyst-fips.global.api.aws'

def test_default_endpoint__region__aws_global_():
    """Default endpoint (region: aws-global)"""
    params = EndpointParams(Region='aws-global')
    result = resolve(params)
    assert result.url == 'https://codecatalyst.global.api.aws'

def test_default_fips_endpoint__region__aws_globa():
    """Default FIPS endpoint (region: aws-global)"""
    params = EndpointParams(Region='aws-global', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://codecatalyst-fips.global.api.aws'

def test_default_endpoint_for_a_valid_home_region():
    """Default endpoint for a valid home region (region: us-west-2)"""
    params = EndpointParams(Region='us-west-2')
    result = resolve(params)
    assert result.url == 'https://codecatalyst.global.api.aws'

def test_default_fips_endpoint_for_a_valid_home_r():
    """Default FIPS endpoint for a valid home region (region: us-west-2)"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://codecatalyst-fips.global.api.aws'

def test_default_endpoint_for_an_unavailable_home():
    """Default endpoint for an unavailable home region (region: us-east-1)"""
    params = EndpointParams(Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://codecatalyst.global.api.aws'

def test_default_fips_endpoint_for_an_unavailable():
    """Default FIPS endpoint for an unavailable home region (region: us-east-1)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://codecatalyst-fips.global.api.aws'