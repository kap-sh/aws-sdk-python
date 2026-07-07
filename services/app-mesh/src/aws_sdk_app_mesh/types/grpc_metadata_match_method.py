"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcMetadataMatchMethod``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.header_match
    import aws_sdk_app_mesh.types.match_range


class _GrpcMetadataMatchMethod_exact(TypedDict, closed=True):
    exact: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


class _GrpcMetadataMatchMethod_regex(TypedDict, closed=True):
    regex: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


class _GrpcMetadataMatchMethod_range(TypedDict, closed=True):
    range: "aws_sdk_app_mesh.types.match_range.MatchRange"


class _GrpcMetadataMatchMethod_prefix(TypedDict, closed=True):
    prefix: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


class _GrpcMetadataMatchMethod_suffix(TypedDict, closed=True):
    suffix: "aws_sdk_app_mesh.types.header_match.HeaderMatch"


GrpcMetadataMatchMethod: TypeAlias = (
    _GrpcMetadataMatchMethod_exact
    | _GrpcMetadataMatchMethod_regex
    | _GrpcMetadataMatchMethod_range
    | _GrpcMetadataMatchMethod_prefix
    | _GrpcMetadataMatchMethod_suffix
)


# --- restJson1 ser/de ---
def serialize_json(value: GrpcMetadataMatchMethod) -> dict:
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
        raise SerializationError("GrpcMetadataMatchMethod: no variant present")


def deserialize_json(data: dict) -> GrpcMetadataMatchMethod:
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
        raise DeserializationError("GrpcMetadataMatchMethod: no recognized variant key")
