"""Generated from Smithy shape ``com.amazonaws.configservice#ExclusionByResourceTypes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_type_list


class ExclusionByResourceTypes(TypedDict):
    resource_types: NotRequired[
        "aws_sdk_config_service.types.resource_type_list.ResourceTypeList"
    ]
    """<p>A comma-separated list of resource types to exclude from recording by the configuration recorder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExclusionByResourceTypes) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import aws_sdk_config_service.types.resource_type_list

        out["resourceTypes"] = (
            aws_sdk_config_service.types.resource_type_list.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExclusionByResourceTypes:
    out: ExclusionByResourceTypes = {}  # type: ignore[typeddict-item]
    if "resourceTypes" in data:
        import aws_sdk_config_service.types.resource_type_list

        out["resource_types"] = (
            aws_sdk_config_service.types.resource_type_list.deserialize_aws_json_1_1(
                data["resourceTypes"]
            )
        )
    return out
