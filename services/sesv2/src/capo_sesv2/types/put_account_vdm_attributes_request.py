"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountVdmAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.vdm_attributes


class PutAccountVdmAttributesRequest(TypedDict, closed=True):
    vdm_attributes: "capo_sesv2.types.vdm_attributes.VdmAttributes"
    """<p>The VDM attributes that you wish to apply to your Amazon SES account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountVdmAttributesRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.vdm_attributes

    out["VdmAttributes"] = capo_sesv2.types.vdm_attributes.serialize_json(
        value["vdm_attributes"]
    )
    return out


def deserialize_json(data: dict) -> PutAccountVdmAttributesRequest:
    out: PutAccountVdmAttributesRequest = {}  # type: ignore[typeddict-item]
    if "VdmAttributes" in data:
        import capo_sesv2.types.vdm_attributes

        out["vdm_attributes"] = capo_sesv2.types.vdm_attributes.deserialize_json(
            data["VdmAttributes"]
        )
    else:
        raise DeserializationError(
            "PutAccountVdmAttributesRequest.vdm_attributes required"
        )
    return out
