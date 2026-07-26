"""Generated from Smithy shape ``com.amazonaws.connect#NextContactMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.quick_connect_contact_data


class _NextContactMetadata_QuickConnectContactData(TypedDict, closed=True):
    QuickConnectContactData: (
        "capo_connect.types.quick_connect_contact_data.QuickConnectContactData"
    )


NextContactMetadata: TypeAlias = _NextContactMetadata_QuickConnectContactData


# --- restJson1 ser/de ---
def serialize_json(value: NextContactMetadata) -> dict:
    if "QuickConnectContactData" in value:
        import capo_connect.types.quick_connect_contact_data

        return {
            "QuickConnectContactData": capo_connect.types.quick_connect_contact_data.serialize_json(
                value["QuickConnectContactData"]
            )
        }
    else:
        raise SerializationError("NextContactMetadata: no variant present")


def deserialize_json(data: dict) -> NextContactMetadata:
    if "QuickConnectContactData" in data:
        import capo_connect.types.quick_connect_contact_data

        return {
            "QuickConnectContactData": capo_connect.types.quick_connect_contact_data.deserialize_json(
                data["QuickConnectContactData"]
            )
        }
    else:
        raise DeserializationError("NextContactMetadata: no recognized variant key")
