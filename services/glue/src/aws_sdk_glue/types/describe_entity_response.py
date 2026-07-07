"""Generated from Smithy shape ``com.amazonaws.glue#DescribeEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.fields_list
    import aws_sdk_glue.types.next_token


class DescribeEntityResponse(TypedDict, closed=True):
    fields: NotRequired["aws_sdk_glue.types.fields_list.FieldsList"]
    """<p>Describes the fields for that connector entity. This is the list of <code>Field</code> objects. <code>Field</code> is very similar to column in a database. The <code>Field</code> object has information about different properties associated with fields in the connector.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.next_token.NextToken"]
    """<p>A continuation token, present if the current segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityResponse) -> dict:
    out: dict = {}
    if "fields" in value:
        import aws_sdk_glue.types.fields_list

        out["Fields"] = aws_sdk_glue.types.fields_list.serialize_aws_json_1_1(
            value["fields"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityResponse:
    out: DescribeEntityResponse = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_glue.types.fields_list

        out["fields"] = aws_sdk_glue.types.fields_list.deserialize_aws_json_1_1(
            data["Fields"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
