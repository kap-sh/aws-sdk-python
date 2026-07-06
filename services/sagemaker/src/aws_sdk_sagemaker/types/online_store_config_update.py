"""Generated from Smithy shape ``com.amazonaws.sagemaker#OnlineStoreConfigUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ttl_duration


class OnlineStoreConfigUpdate(TypedDict, closed=True):
    ttl_duration: NotRequired["aws_sdk_sagemaker.types.ttl_duration.TtlDuration"]
    r"""<p>Time to live duration, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html\">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnlineStoreConfigUpdate) -> dict:
    out: dict = {}
    if "ttl_duration" in value:
        import aws_sdk_sagemaker.types.ttl_duration

        out["TtlDuration"] = (
            aws_sdk_sagemaker.types.ttl_duration.serialize_aws_json_1_1(
                value["ttl_duration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnlineStoreConfigUpdate:
    out: OnlineStoreConfigUpdate = {}  # type: ignore[typeddict-item]
    if "TtlDuration" in data:
        import aws_sdk_sagemaker.types.ttl_duration

        out["ttl_duration"] = (
            aws_sdk_sagemaker.types.ttl_duration.deserialize_aws_json_1_1(
                data["TtlDuration"]
            )
        )
    return out
