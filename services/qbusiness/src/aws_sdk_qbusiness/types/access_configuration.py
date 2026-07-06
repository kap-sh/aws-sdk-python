"""Generated from Smithy shape ``com.amazonaws.qbusiness#AccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.access_controls
    import aws_sdk_qbusiness.types.member_relation


class AccessConfiguration(TypedDict, closed=True):
    access_controls: "aws_sdk_qbusiness.types.access_controls.AccessControls"
    """<p>A list of <code>AccessControlList</code> objects.</p>"""
    member_relation: NotRequired[
        "aws_sdk_qbusiness.types.member_relation.MemberRelation"
    ]
    """<p>Describes the member relation within the <code>AccessControlList</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.access_controls

    out["accessControls"] = aws_sdk_qbusiness.types.access_controls.serialize_json(
        value["access_controls"]
    )
    if "member_relation" in value:
        import aws_sdk_qbusiness.types.member_relation

        out["memberRelation"] = aws_sdk_qbusiness.types.member_relation.serialize_json(
            value["member_relation"]
        )
    return out


def deserialize_json(data: dict) -> AccessConfiguration:
    out: AccessConfiguration = {}  # type: ignore[typeddict-item]
    if "accessControls" in data:
        import aws_sdk_qbusiness.types.access_controls

        out["access_controls"] = (
            aws_sdk_qbusiness.types.access_controls.deserialize_json(
                data["accessControls"]
            )
        )
    else:
        raise DeserializationError("AccessConfiguration.access_controls required")
    if "memberRelation" in data:
        import aws_sdk_qbusiness.types.member_relation

        out["member_relation"] = (
            aws_sdk_qbusiness.types.member_relation.deserialize_json(
                data["memberRelation"]
            )
        )
    return out
