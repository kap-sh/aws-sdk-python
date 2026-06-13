"""Generated from Smithy shape ``com.amazonaws.appmesh#SubjectAlternativeNames``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.subject_alternative_name_matchers


class SubjectAlternativeNames(TypedDict):
    match: "aws_sdk_app_mesh.types.subject_alternative_name_matchers.SubjectAlternativeNameMatchers"
    """<p>An object that represents the criteria for determining a SANs match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectAlternativeNames) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.subject_alternative_name_matchers

    out["match"] = (
        aws_sdk_app_mesh.types.subject_alternative_name_matchers.serialize_json(
            value["match"]
        )
    )
    return out


def deserialize_json(data: dict) -> SubjectAlternativeNames:
    out: SubjectAlternativeNames = {}  # type: ignore[typeddict-item]
    if "match" in data:
        import aws_sdk_app_mesh.types.subject_alternative_name_matchers

        out["match"] = (
            aws_sdk_app_mesh.types.subject_alternative_name_matchers.deserialize_json(
                data["match"]
            )
        )
    else:
        raise DeserializationError("SubjectAlternativeNames.match required")
    return out
