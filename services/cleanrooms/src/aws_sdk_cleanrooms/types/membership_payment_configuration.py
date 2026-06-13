"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipPaymentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_job_compute_payment_config
    import aws_sdk_cleanrooms.types.membership_ml_payment_config
    import aws_sdk_cleanrooms.types.membership_query_compute_payment_config


class MembershipPaymentConfiguration(TypedDict):
    query_compute: "aws_sdk_cleanrooms.types.membership_query_compute_payment_config.MembershipQueryComputePaymentConfig"
    """<p>The payment responsibilities accepted by the collaboration member for query compute costs.</p>"""
    machine_learning: NotRequired[
        "aws_sdk_cleanrooms.types.membership_ml_payment_config.MembershipMLPaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the collaboration member for machine learning costs.</p>"""
    job_compute: NotRequired[
        "aws_sdk_cleanrooms.types.membership_job_compute_payment_config.MembershipJobComputePaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the collaboration member for job compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipPaymentConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.membership_query_compute_payment_config

    out["queryCompute"] = (
        aws_sdk_cleanrooms.types.membership_query_compute_payment_config.serialize_json(
            value["query_compute"]
        )
    )
    if "machine_learning" in value:
        import aws_sdk_cleanrooms.types.membership_ml_payment_config

        out["machineLearning"] = (
            aws_sdk_cleanrooms.types.membership_ml_payment_config.serialize_json(
                value["machine_learning"]
            )
        )
    if "job_compute" in value:
        import aws_sdk_cleanrooms.types.membership_job_compute_payment_config

        out["jobCompute"] = (
            aws_sdk_cleanrooms.types.membership_job_compute_payment_config.serialize_json(
                value["job_compute"]
            )
        )
    return out


def deserialize_json(data: dict) -> MembershipPaymentConfiguration:
    out: MembershipPaymentConfiguration = {}  # type: ignore[typeddict-item]
    if "queryCompute" in data:
        import aws_sdk_cleanrooms.types.membership_query_compute_payment_config

        out["query_compute"] = (
            aws_sdk_cleanrooms.types.membership_query_compute_payment_config.deserialize_json(
                data["queryCompute"]
            )
        )
    else:
        raise DeserializationError(
            "MembershipPaymentConfiguration.query_compute required"
        )
    if "machineLearning" in data:
        import aws_sdk_cleanrooms.types.membership_ml_payment_config

        out["machine_learning"] = (
            aws_sdk_cleanrooms.types.membership_ml_payment_config.deserialize_json(
                data["machineLearning"]
            )
        )
    if "jobCompute" in data:
        import aws_sdk_cleanrooms.types.membership_job_compute_payment_config

        out["job_compute"] = (
            aws_sdk_cleanrooms.types.membership_job_compute_payment_config.deserialize_json(
                data["jobCompute"]
            )
        )
    return out
