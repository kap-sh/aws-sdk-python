"""Generated from Smithy shape ``com.amazonaws.configservice#PutStoredQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.stored_query
    import aws_sdk_config_service.types.tags_list


class PutStoredQueryRequest(TypedDict, closed=True):
    stored_query: "aws_sdk_config_service.types.stored_query.StoredQuery"
    """<p>A list of <code>StoredQuery</code> objects. The mandatory fields are <code>QueryName</code> and <code>Expression</code>.</p> <note> <p>When you are creating a query, you must provide a query name and an expression. When you are updating a query, you must provide a query name but updating the description is optional.</p> </note>"""
    tags: NotRequired["aws_sdk_config_service.types.tags_list.TagsList"]
    """<p>A list of <code>Tags</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutStoredQueryRequest) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.stored_query

    out["StoredQuery"] = (
        aws_sdk_config_service.types.stored_query.serialize_aws_json_1_1(
            value["stored_query"]
        )
    )
    if "tags" in value:
        import aws_sdk_config_service.types.tags_list

        out["Tags"] = aws_sdk_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutStoredQueryRequest:
    out: PutStoredQueryRequest = {}  # type: ignore[typeddict-item]
    if "StoredQuery" in data:
        import aws_sdk_config_service.types.stored_query

        out["stored_query"] = (
            aws_sdk_config_service.types.stored_query.deserialize_aws_json_1_1(
                data["StoredQuery"]
            )
        )
    else:
        raise DeserializationError("PutStoredQueryRequest.stored_query required")
    if "Tags" in data:
        import aws_sdk_config_service.types.tags_list

        out["tags"] = aws_sdk_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
