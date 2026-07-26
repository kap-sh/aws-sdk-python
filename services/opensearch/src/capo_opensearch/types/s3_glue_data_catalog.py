"""Generated from Smithy shape ``com.amazonaws.opensearch#S3GlueDataCatalog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.role_arn


class S3GlueDataCatalog(TypedDict, closed=True):
    role_arn: NotRequired["capo_opensearch.types.role_arn.RoleArn"]
    """<p>>The Amazon Resource Name (ARN) for the S3 Glue Data Catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3GlueDataCatalog) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> S3GlueDataCatalog:
    out: S3GlueDataCatalog = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
