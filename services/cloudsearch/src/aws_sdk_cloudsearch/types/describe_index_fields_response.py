"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeIndexFieldsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.index_field_status_list


class DescribeIndexFieldsResponse(TypedDict):
    index_fields: (
        "aws_sdk_cloudsearch.types.index_field_status_list.IndexFieldStatusList"
    )
    """<p>The index fields configured for the domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeIndexFieldsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.index_field_status_list

    aws_sdk_cloudsearch.types.index_field_status_list.serialize_query(
        value["index_fields"], pairs, f"{prefix}.IndexFields"
    )


def deserialize_query(el: Element) -> DescribeIndexFieldsResponse:
    out: DescribeIndexFieldsResponse = {}  # type: ignore[typeddict-item]
    child_index_fields = el.find("IndexFields")
    if child_index_fields is not None:
        import aws_sdk_cloudsearch.types.index_field_status_list

        out["index_fields"] = (
            aws_sdk_cloudsearch.types.index_field_status_list.deserialize_query(
                child_index_fields
            )
        )
    else:
        raise DeserializationError("DescribeIndexFieldsResponse.index_fields required")
    return out
