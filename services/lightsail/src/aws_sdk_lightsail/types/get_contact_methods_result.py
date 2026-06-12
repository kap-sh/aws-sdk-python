"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContactMethodsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.contact_methods_list


class GetContactMethodsResult(TypedDict):
    contact_methods: NotRequired[
        "aws_sdk_lightsail.types.contact_methods_list.ContactMethodsList"
    ]
    """<p>An array of objects that describe the contact methods.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactMethodsResult) -> dict:
    out: dict = {}
    if "contact_methods" in value:
        import aws_sdk_lightsail.types.contact_methods_list

        out["contactMethods"] = (
            aws_sdk_lightsail.types.contact_methods_list.serialize_aws_json_1_1(
                value["contact_methods"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactMethodsResult:
    out: GetContactMethodsResult = {}  # type: ignore[typeddict-item]
    if "contactMethods" in data:
        import aws_sdk_lightsail.types.contact_methods_list

        out["contact_methods"] = (
            aws_sdk_lightsail.types.contact_methods_list.deserialize_aws_json_1_1(
                data["contactMethods"]
            )
        )
    return out
