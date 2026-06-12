"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseEventIncludedData``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_identifier_list


class CaseEventIncludedData(TypedDict):
    fields: "aws_sdk_connectcases.types.field_identifier_list.FieldIdentifierList"
    """<p>List of field identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseEventIncludedData) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.field_identifier_list

    out["fields"] = aws_sdk_connectcases.types.field_identifier_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> CaseEventIncludedData:
    out: CaseEventIncludedData = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.field_identifier_list

        out["fields"] = (
            aws_sdk_connectcases.types.field_identifier_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("CaseEventIncludedData.fields required")
    return out
