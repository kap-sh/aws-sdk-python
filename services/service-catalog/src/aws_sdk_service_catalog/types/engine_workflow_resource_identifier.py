"""Generated from Smithy shape ``com.amazonaws.servicecatalog#EngineWorkflowResourceIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.unique_tag_resource_identifier


class EngineWorkflowResourceIdentifier(TypedDict):
    unique_tag: NotRequired[
        "aws_sdk_service_catalog.types.unique_tag_resource_identifier.UniqueTagResourceIdentifier"
    ]
    """<p> The unique key-value pair for a tag that identifies provisioned product resources. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineWorkflowResourceIdentifier) -> dict:
    out: dict = {}
    if "unique_tag" in value:
        import aws_sdk_service_catalog.types.unique_tag_resource_identifier

        out["UniqueTag"] = (
            aws_sdk_service_catalog.types.unique_tag_resource_identifier.serialize_aws_json_1_1(
                value["unique_tag"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EngineWorkflowResourceIdentifier:
    out: EngineWorkflowResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "UniqueTag" in data:
        import aws_sdk_service_catalog.types.unique_tag_resource_identifier

        out["unique_tag"] = (
            aws_sdk_service_catalog.types.unique_tag_resource_identifier.deserialize_aws_json_1_1(
                data["UniqueTag"]
            )
        )
    return out
