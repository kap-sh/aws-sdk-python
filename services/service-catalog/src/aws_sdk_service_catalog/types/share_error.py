"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ShareError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.error
    import aws_sdk_service_catalog.types.message
    import aws_sdk_service_catalog.types.namespaces


class ShareError(TypedDict):
    accounts: NotRequired["aws_sdk_service_catalog.types.namespaces.Namespaces"]
    """<p>List of accounts impacted by the error.</p>"""
    message: NotRequired["aws_sdk_service_catalog.types.message.Message"]
    """<p>Information about the error.</p>"""
    error: NotRequired["aws_sdk_service_catalog.types.error.Error"]
    """<p>Error type that happened when processing the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareError) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_service_catalog.types.namespaces

        out["Accounts"] = (
            aws_sdk_service_catalog.types.namespaces.serialize_aws_json_1_1(
                value["accounts"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ShareError:
    out: ShareError = {}  # type: ignore[typeddict-item]
    if "Accounts" in data:
        import aws_sdk_service_catalog.types.namespaces

        out["accounts"] = (
            aws_sdk_service_catalog.types.namespaces.deserialize_aws_json_1_1(
                data["Accounts"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Error" in data:
        out["error"] = data["Error"]
    return out
