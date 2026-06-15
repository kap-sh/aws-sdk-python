"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CustomerManagedPolicyReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.managed_policy_name
    import aws_sdk_sso_admin.types.managed_policy_path


class CustomerManagedPolicyReference(TypedDict):
    name: "aws_sdk_sso_admin.types.managed_policy_name.ManagedPolicyName"
    """<p>The name of the IAM policy that you have configured in each account where you want to deploy your permission set.</p>"""
    path: NotRequired["aws_sdk_sso_admin.types.managed_policy_path.ManagedPolicyPath"]
    r"""<p>The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is <code>/</code>. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names\">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerManagedPolicyReference) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerManagedPolicyReference:
    out: CustomerManagedPolicyReference = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CustomerManagedPolicyReference.name required")
    if "Path" in data:
        out["path"] = data["Path"]
    return out
