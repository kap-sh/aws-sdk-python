"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.policy_name_type
    import aws_sdk_kms.types.policy_type


class GetKeyPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_kms.types.policy_type.PolicyType"]
    """<p>A key policy document in JSON format.</p>"""
    policy_name: NotRequired["aws_sdk_kms.types.policy_name_type.PolicyNameType"]
    """<p>The name of the key policy. The only valid value is <code>default</code>.</p>"""
