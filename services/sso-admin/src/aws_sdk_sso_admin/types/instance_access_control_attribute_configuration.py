"""Generated from Smithy shape ``com.amazonaws.ssoadmin#InstanceAccessControlAttributeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.access_control_attribute_list


class InstanceAccessControlAttributeConfiguration(TypedDict, closed=True):
    access_control_attributes: "aws_sdk_sso_admin.types.access_control_attribute_list.AccessControlAttributeList"
    """<p>Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAccessControlAttributeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_sso_admin.types.access_control_attribute_list

    out["AccessControlAttributes"] = (
        aws_sdk_sso_admin.types.access_control_attribute_list.serialize_aws_json_1_1(
            value["access_control_attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAccessControlAttributeConfiguration:
    out: InstanceAccessControlAttributeConfiguration = {}  # type: ignore[typeddict-item]
    if "AccessControlAttributes" in data:
        import aws_sdk_sso_admin.types.access_control_attribute_list

        out["access_control_attributes"] = (
            aws_sdk_sso_admin.types.access_control_attribute_list.deserialize_aws_json_1_1(
                data["AccessControlAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "InstanceAccessControlAttributeConfiguration.access_control_attributes required"
        )
    return out
