"""Generated from Smithy shape ``com.amazonaws.kms#DescribeKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.key_metadata


class DescribeKeyResponse(TypedDict, closed=True):
    key_metadata: NotRequired["capo_kms.types.key_metadata.KeyMetadata"]
    """<p>Metadata associated with the key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeKeyResponse) -> dict:
    out: dict = {}
    if "key_metadata" in value:
        import capo_kms.types.key_metadata

        out["KeyMetadata"] = capo_kms.types.key_metadata.serialize_aws_json_1_1(
            value["key_metadata"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeKeyResponse:
    out: DescribeKeyResponse = {}  # type: ignore[typeddict-item]
    if "KeyMetadata" in data:
        import capo_kms.types.key_metadata

        out["key_metadata"] = capo_kms.types.key_metadata.deserialize_aws_json_1_1(
            data["KeyMetadata"]
        )
    return out
