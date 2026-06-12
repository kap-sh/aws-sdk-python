"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Facets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.string
    import aws_sdk_cloudsearch_domain.types.bucket_info

Facets: TypeAlias = dict[
    "aws_sdk_cloudsearch_domain.types.string.String",
    "aws_sdk_cloudsearch_domain.types.bucket_info.BucketInfo",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Facets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_cloudsearch_domain.types.bucket_info

        out[key] = aws_sdk_cloudsearch_domain.types.bucket_info.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Facets:
    out: Facets = {}
    for key, value in data.items():
        import aws_sdk_cloudsearch_domain.types.bucket_info

        out[key] = aws_sdk_cloudsearch_domain.types.bucket_info.deserialize_json(value)
    return out
