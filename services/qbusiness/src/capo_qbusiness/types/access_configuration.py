"""Generated from Smithy shape ``com.amazonaws.qbusiness#AccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.access_controls
    import capo_qbusiness.types.member_relation


class AccessConfiguration(TypedDict, closed=True):
    access_controls: "capo_qbusiness.types.access_controls.AccessControls"
    """<p>A list of <code>AccessControlList</code> objects.</p>"""
    member_relation: NotRequired["capo_qbusiness.types.member_relation.MemberRelation"]
    """<p>Describes the member relation within the <code>AccessControlList</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.access_controls

    out["accessControls"] = capo_qbusiness.types.access_controls.serialize_json(
        value["access_controls"]
    )
    if "member_relation" in value:
        import capo_qbusiness.types.member_relation

        out["memberRelation"] = capo_qbusiness.types.member_relation.serialize_json(
            value["member_relation"]
        )
    return out


def deserialize_json(data: dict) -> AccessConfiguration:
    out: AccessConfiguration = {}  # type: ignore[typeddict-item]
    if "accessControls" in data:
        import capo_qbusiness.types.access_controls

        out["access_controls"] = capo_qbusiness.types.access_controls.deserialize_json(
            data["accessControls"]
        )
    else:
        raise DeserializationError("AccessConfiguration.access_controls required")
    if "memberRelation" in data:
        import capo_qbusiness.types.member_relation

        out["member_relation"] = capo_qbusiness.types.member_relation.deserialize_json(
            data["memberRelation"]
        )
    return out
