"""Generated from Smithy shape ``com.amazonaws.appmesh#SubjectAlternativeNameMatchers``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.subject_alternative_name_list


class SubjectAlternativeNameMatchers(TypedDict):
    exact: "aws_sdk_app_mesh.types.subject_alternative_name_list.SubjectAlternativeNameList"
    """<p>The values sent must match the specified values exactly.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectAlternativeNameMatchers) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.subject_alternative_name_list

    out["exact"] = aws_sdk_app_mesh.types.subject_alternative_name_list.serialize_json(
        value["exact"]
    )
    return out


def deserialize_json(data: dict) -> SubjectAlternativeNameMatchers:
    out: SubjectAlternativeNameMatchers = {}  # type: ignore[typeddict-item]
    if "exact" in data:
        import aws_sdk_app_mesh.types.subject_alternative_name_list

        out["exact"] = (
            aws_sdk_app_mesh.types.subject_alternative_name_list.deserialize_json(
                data["exact"]
            )
        )
    else:
        raise DeserializationError("SubjectAlternativeNameMatchers.exact required")
    return out
