"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseEventIncludedData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.field_identifier_list


class CaseEventIncludedData(TypedDict, closed=True):
    fields: "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
    """<p>List of field identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseEventIncludedData) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_identifier_list

    out["fields"] = capo_connectcases.types.field_identifier_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> CaseEventIncludedData:
    out: CaseEventIncludedData = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import capo_connectcases.types.field_identifier_list

        out["fields"] = capo_connectcases.types.field_identifier_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("CaseEventIncludedData.fields required")
    return out
