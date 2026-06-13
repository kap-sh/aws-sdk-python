"""Generated from Smithy shape ``com.amazonaws.braket#SearchJobsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.search_jobs_filter_operator
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.string256_list


class SearchJobsFilter(TypedDict):
    name: "aws_sdk_braket.types.string64.String64"
    """<p>The name of the hybrid job parameter to filter based on. Filter name can be either <code>jobArn</code> or <code>createdAt</code>. </p>"""
    values: "aws_sdk_braket.types.string256_list.String256List"
    """<p>The values used to filter hybrid jobs based on the filter name and operator.</p>"""
    operator: (
        "aws_sdk_braket.types.search_jobs_filter_operator.SearchJobsFilterOperator"
    )
    """<p>An operator to use for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_braket.types.string256_list

    out["values"] = aws_sdk_braket.types.string256_list.serialize_json(value["values"])
    out["operator"] = value["operator"]
    return out


def deserialize_json(data: dict) -> SearchJobsFilter:
    out: SearchJobsFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SearchJobsFilter.name required")
    if "values" in data:
        import aws_sdk_braket.types.string256_list

        out["values"] = aws_sdk_braket.types.string256_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("SearchJobsFilter.values required")
    if "operator" in data:
        out["operator"] = data["operator"]
    else:
        raise DeserializationError("SearchJobsFilter.operator required")
    return out
