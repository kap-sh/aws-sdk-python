"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PaymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.job_compute_payment_config
    import aws_sdk_cleanrooms.types.ml_payment_config
    import aws_sdk_cleanrooms.types.query_compute_payment_config


class PaymentConfiguration(TypedDict, closed=True):
    query_compute: "aws_sdk_cleanrooms.types.query_compute_payment_config.QueryComputePaymentConfig"
    """<p>The collaboration member's payment responsibilities set by the collaboration creator for query compute costs.</p>"""
    machine_learning: NotRequired[
        "aws_sdk_cleanrooms.types.ml_payment_config.MLPaymentConfig"
    ]
    """<p>An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.</p>"""
    job_compute: NotRequired[
        "aws_sdk_cleanrooms.types.job_compute_payment_config.JobComputePaymentConfig"
    ]
    """<p> The compute configuration for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.query_compute_payment_config

    out["queryCompute"] = (
        aws_sdk_cleanrooms.types.query_compute_payment_config.serialize_json(
            value["query_compute"]
        )
    )
    if "machine_learning" in value:
        import aws_sdk_cleanrooms.types.ml_payment_config

        out["machineLearning"] = (
            aws_sdk_cleanrooms.types.ml_payment_config.serialize_json(
                value["machine_learning"]
            )
        )
    if "job_compute" in value:
        import aws_sdk_cleanrooms.types.job_compute_payment_config

        out["jobCompute"] = (
            aws_sdk_cleanrooms.types.job_compute_payment_config.serialize_json(
                value["job_compute"]
            )
        )
    return out


def deserialize_json(data: dict) -> PaymentConfiguration:
    out: PaymentConfiguration = {}  # type: ignore[typeddict-item]
    if "queryCompute" in data:
        import aws_sdk_cleanrooms.types.query_compute_payment_config

        out["query_compute"] = (
            aws_sdk_cleanrooms.types.query_compute_payment_config.deserialize_json(
                data["queryCompute"]
            )
        )
    else:
        raise DeserializationError("PaymentConfiguration.query_compute required")
    if "machineLearning" in data:
        import aws_sdk_cleanrooms.types.ml_payment_config

        out["machine_learning"] = (
            aws_sdk_cleanrooms.types.ml_payment_config.deserialize_json(
                data["machineLearning"]
            )
        )
    if "jobCompute" in data:
        import aws_sdk_cleanrooms.types.job_compute_payment_config

        out["job_compute"] = (
            aws_sdk_cleanrooms.types.job_compute_payment_config.deserialize_json(
                data["jobCompute"]
            )
        )
    return out
