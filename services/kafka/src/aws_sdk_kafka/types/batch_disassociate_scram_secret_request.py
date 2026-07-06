"""Generated from Smithy shape ``com.amazonaws.kafka#BatchDisassociateScramSecretRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__string


class BatchDisassociateScramSecretRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>"""
    secret_arn_list: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>List of AWS Secrets Manager secret ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateScramSecretRequest) -> dict:
    out: dict = {}
    if "secret_arn_list" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["secretArnList"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["secret_arn_list"]
        )
    return out


def deserialize_json(data: dict) -> BatchDisassociateScramSecretRequest:
    out: BatchDisassociateScramSecretRequest = {}  # type: ignore[typeddict-item]
    if "secretArnList" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["secret_arn_list"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["secretArnList"]
        )
    return out
