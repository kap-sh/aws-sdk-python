"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipPaymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_job_compute_payment_config
    import capo_cleanrooms.types.membership_ml_payment_config
    import capo_cleanrooms.types.membership_query_compute_payment_config


class MembershipPaymentConfiguration(TypedDict, closed=True):
    query_compute: "capo_cleanrooms.types.membership_query_compute_payment_config.MembershipQueryComputePaymentConfig"
    """<p>The payment responsibilities accepted by the collaboration member for query compute costs.</p>"""
    machine_learning: NotRequired[
        "capo_cleanrooms.types.membership_ml_payment_config.MembershipMLPaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the collaboration member for machine learning costs.</p>"""
    job_compute: NotRequired[
        "capo_cleanrooms.types.membership_job_compute_payment_config.MembershipJobComputePaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the collaboration member for job compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipPaymentConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.membership_query_compute_payment_config

    out["queryCompute"] = (
        capo_cleanrooms.types.membership_query_compute_payment_config.serialize_json(
            value["query_compute"]
        )
    )
    if "machine_learning" in value:
        import capo_cleanrooms.types.membership_ml_payment_config

        out["machineLearning"] = (
            capo_cleanrooms.types.membership_ml_payment_config.serialize_json(
                value["machine_learning"]
            )
        )
    if "job_compute" in value:
        import capo_cleanrooms.types.membership_job_compute_payment_config

        out["jobCompute"] = (
            capo_cleanrooms.types.membership_job_compute_payment_config.serialize_json(
                value["job_compute"]
            )
        )
    return out


def deserialize_json(data: dict) -> MembershipPaymentConfiguration:
    out: MembershipPaymentConfiguration = {}  # type: ignore[typeddict-item]
    if "queryCompute" in data:
        import capo_cleanrooms.types.membership_query_compute_payment_config

        out["query_compute"] = (
            capo_cleanrooms.types.membership_query_compute_payment_config.deserialize_json(
                data["queryCompute"]
            )
        )
    else:
        raise DeserializationError(
            "MembershipPaymentConfiguration.query_compute required"
        )
    if "machineLearning" in data:
        import capo_cleanrooms.types.membership_ml_payment_config

        out["machine_learning"] = (
            capo_cleanrooms.types.membership_ml_payment_config.deserialize_json(
                data["machineLearning"]
            )
        )
    if "jobCompute" in data:
        import capo_cleanrooms.types.membership_job_compute_payment_config

        out["job_compute"] = (
            capo_cleanrooms.types.membership_job_compute_payment_config.deserialize_json(
                data["jobCompute"]
            )
        )
    return out
