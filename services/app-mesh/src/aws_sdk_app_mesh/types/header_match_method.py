"""Generated from Smithy shape ``com.amazonaws.appmesh#HeaderMatchMethod``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.header_match
    import aws_sdk_app_mesh.types.match_range


class _HeaderMatchMethod_exact(TypedDict):
    exact: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


class _HeaderMatchMethod_regex(TypedDict):
    regex: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


class _HeaderMatchMethod_range(TypedDict):
    range: "aws_sdk_app_mesh.types.match_range.MatchRange"


class _HeaderMatchMethod_prefix(TypedDict):
    prefix: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


class _HeaderMatchMethod_suffix(TypedDict):
    suffix: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


HeaderMatchMethod: TypeAlias = (
    _HeaderMatchMethod_exact
    | _HeaderMatchMethod_regex
    | _HeaderMatchMethod_range
    | _HeaderMatchMethod_prefix
    | _HeaderMatchMethod_suffix
)


# --- restJson1 ser/de ---
def serialize_json(value: HeaderMatchMethod) -> dict:
    if "exact" in value:
        return {"exact": value["exact"]}
    elif "regex" in value:
        return {"regex": value["regex"]}
    elif "range" in value:
        import aws_sdk_app_mesh.types.match_range

        return {
            "range": aws_sdk_app_mesh.types.match_range.serialize_json(value["range"])
        }
    elif "prefix" in value:
        return {"prefix": value["prefix"]}
    elif "suffix" in value:
        return {"suffix": value["suffix"]}
    else:
        raise SerializationError("HeaderMatchMethod: no variant present")


def deserialize_json(data: dict) -> HeaderMatchMethod:
    if "exact" in data:
        return {"exact": data["exact"]}
    elif "regex" in data:
        return {"regex": data["regex"]}
    elif "range" in data:
        import aws_sdk_app_mesh.types.match_range

        return {
            "range": aws_sdk_app_mesh.types.match_range.deserialize_json(data["range"])
        }
    elif "prefix" in data:
        return {"prefix": data["prefix"]}
    elif "suffix" in data:
        return {"suffix": data["suffix"]}
    else:
        raise DeserializationError("HeaderMatchMethod: no recognized variant key")
