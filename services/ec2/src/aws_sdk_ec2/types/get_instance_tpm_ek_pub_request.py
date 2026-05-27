"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTpmEkPubRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ek_pub_key_format
    import aws_sdk_ec2.types.ek_pub_key_type
    import aws_sdk_ec2.types.instance_id


class GetInstanceTpmEkPubRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance for which to get the public endorsement key.</p>"""
    key_type: NotRequired["aws_sdk_ec2.types.ek_pub_key_type.EkPubKeyType"]
    """<p>The required public endorsement key type.</p>"""
    key_format: NotRequired["aws_sdk_ec2.types.ek_pub_key_format.EkPubKeyFormat"]
    """<p>The required public endorsement key format. Specify <code>der</code> for a DER-encoded public key that is compatible with OpenSSL. Specify <code>tpmt</code> for a TPM 2.0 format that is compatible with tpm2-tools. The returned key is base64 encoded.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specify this parameter to verify whether the request will succeed, without actually making the request. If the request will succeed, the response is <code>DryRunOperation</code>. Otherwise, the response is <code>UnauthorizedOperation</code>.</p>"""
