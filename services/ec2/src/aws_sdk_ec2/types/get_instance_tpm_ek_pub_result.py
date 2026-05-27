"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTpmEkPubResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ek_pub_key_format
    import aws_sdk_ec2.types.ek_pub_key_type
    import aws_sdk_ec2.types.ek_pub_key_value
    import aws_sdk_ec2.types.instance_id


class GetInstanceTpmEkPubResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    key_type: NotRequired["aws_sdk_ec2.types.ek_pub_key_type.EkPubKeyType"]
    """<p>The public endorsement key type.</p>"""
    key_format: NotRequired["aws_sdk_ec2.types.ek_pub_key_format.EkPubKeyFormat"]
    """<p>The public endorsement key format.</p>"""
    key_value: NotRequired["aws_sdk_ec2.types.ek_pub_key_value.EkPubKeyValue"]
    """<p>The public endorsement key material.</p>"""
