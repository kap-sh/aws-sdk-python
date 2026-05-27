"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyEbsDefaultKmsKeyIdRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.kms_key_id


class ModifyEbsDefaultKmsKeyIdRequest(TypedDict):
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Amazon EBS is used. If <code>KmsKeyId</code> is specified, the encrypted state must be <code>true</code>.</p> <p>You can specify the KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
