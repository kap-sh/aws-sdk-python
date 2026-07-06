"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.batch_get_field_identifier_list
    import aws_sdk_connectcases.types.domain_id


class BatchGetFieldRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    fields: "aws_sdk_connectcases.types.batch_get_field_identifier_list.BatchGetFieldIdentifierList"
    """<p>A list of unique field identifiers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.batch_get_field_identifier_list

    out["fields"] = (
        aws_sdk_connectcases.types.batch_get_field_identifier_list.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFieldRequest:
    out: BatchGetFieldRequest = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.batch_get_field_identifier_list

        out["fields"] = (
            aws_sdk_connectcases.types.batch_get_field_identifier_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("BatchGetFieldRequest.fields required")
    return out
