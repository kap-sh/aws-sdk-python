"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateServiceActionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.service_action_detail


class CreateServiceActionOutput(TypedDict):
    service_action_detail: NotRequired[
        "aws_sdk_service_catalog.types.service_action_detail.ServiceActionDetail"
    ]
    """<p>An object containing information about the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServiceActionOutput) -> dict:
    out: dict = {}
    if "service_action_detail" in value:
        import aws_sdk_service_catalog.types.service_action_detail

        out["ServiceActionDetail"] = (
            aws_sdk_service_catalog.types.service_action_detail.serialize_aws_json_1_1(
                value["service_action_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateServiceActionOutput:
    out: CreateServiceActionOutput = {}  # type: ignore[typeddict-item]
    if "ServiceActionDetail" in data:
        import aws_sdk_service_catalog.types.service_action_detail

        out["service_action_detail"] = (
            aws_sdk_service_catalog.types.service_action_detail.deserialize_aws_json_1_1(
                data["ServiceActionDetail"]
            )
        )
    return out
