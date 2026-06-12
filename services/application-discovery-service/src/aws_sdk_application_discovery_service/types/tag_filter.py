"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#TagFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.filter_name
    import aws_sdk_application_discovery_service.types.filter_values


class TagFilter(TypedDict):
    name: "aws_sdk_application_discovery_service.types.filter_name.FilterName"
    """<p>A name of the tag filter.</p>"""
    values: "aws_sdk_application_discovery_service.types.filter_values.FilterValues"
    """<p>Values for the tag filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_application_discovery_service.types.filter_values

    out["values"] = (
        aws_sdk_application_discovery_service.types.filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TagFilter.name required")
    if "values" in data:
        import aws_sdk_application_discovery_service.types.filter_values

        out["values"] = (
            aws_sdk_application_discovery_service.types.filter_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    else:
        raise DeserializationError("TagFilter.values required")
    return out
