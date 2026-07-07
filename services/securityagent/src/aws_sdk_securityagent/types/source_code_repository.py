"""Generated from Smithy shape ``com.amazonaws.securityagent#SourceCodeRepository``."""

from typing_extensions import NotRequired, TypedDict


class SourceCodeRepository(TypedDict, closed=True):
    s3_location: NotRequired["str"]
    """<p>The Amazon S3 location of the source code repository archive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceCodeRepository) -> dict:
    out: dict = {}
    if "s3_location" in value:
        out["s3Location"] = value["s3_location"]
    return out


def deserialize_json(data: dict) -> SourceCodeRepository:
    out: SourceCodeRepository = {}  # type: ignore[typeddict-item]
    if "s3Location" in data:
        out["s3_location"] = data["s3Location"]
    return out
