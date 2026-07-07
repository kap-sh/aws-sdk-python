"""Generated from Smithy shape ``com.amazonaws.sagemaker#OidcMemberDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.groups


class OidcMemberDefinition(TypedDict, closed=True):
    groups: NotRequired["aws_sdk_sagemaker.types.groups.Groups"]
    """<p>A list of comma seperated strings that identifies user groups in your OIDC IdP. Each user group is made up of a group of private workers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OidcMemberDefinition) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_sagemaker.types.groups

        out["Groups"] = aws_sdk_sagemaker.types.groups.serialize_aws_json_1_1(
            value["groups"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OidcMemberDefinition:
    out: OidcMemberDefinition = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_sagemaker.types.groups

        out["groups"] = aws_sdk_sagemaker.types.groups.deserialize_aws_json_1_1(
            data["Groups"]
        )
    return out
