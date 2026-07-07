"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.non_empty_string
    import aws_sdk_elasticsearch_service.types.value_string_list


class Filter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_elasticsearch_service.types.non_empty_string.NonEmptyString"
    ]
    """<p> Specifies the name of the filter. </p>"""
    values: NotRequired[
        "aws_sdk_elasticsearch_service.types.value_string_list.ValueStringList"
    ]
    """<p> Contains one or more values for the filter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_elasticsearch_service.types.value_string_list

        out["Values"] = (
            aws_sdk_elasticsearch_service.types.value_string_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_elasticsearch_service.types.value_string_list

        out["values"] = (
            aws_sdk_elasticsearch_service.types.value_string_list.deserialize_json(
                data["Values"]
            )
        )
    return out
