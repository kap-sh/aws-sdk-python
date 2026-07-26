"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.instance


class DeleteInstanceResponse(TypedDict, closed=True):
    instance: "capo_supplychain.types.instance.Instance"
    """<p>The AWS Supply Chain instance resource data details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInstanceResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.instance

    out["instance"] = capo_supplychain.types.instance.serialize_json(value["instance"])
    return out


def deserialize_json(data: dict) -> DeleteInstanceResponse:
    out: DeleteInstanceResponse = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import capo_supplychain.types.instance

        out["instance"] = capo_supplychain.types.instance.deserialize_json(
            data["instance"]
        )
    else:
        raise DeserializationError("DeleteInstanceResponse.instance required")
    return out
