"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.currency_code
    import capo_sagemaker.types.reserved_capacity_offerings
    import capo_sagemaker.types.sage_maker_resource_names
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_plan_duration_hours
    import capo_sagemaker.types.training_plan_duration_minutes
    import capo_sagemaker.types.training_plan_offering_id


class TrainingPlanOffering(TypedDict, closed=True):
    training_plan_offering_id: NotRequired[
        "capo_sagemaker.types.training_plan_offering_id.TrainingPlanOfferingId"
    ]
    """<p>The unique identifier for this training plan offering.</p>"""
    target_resources: NotRequired[
        "capo_sagemaker.types.sage_maker_resource_names.SageMakerResourceNames"
    ]
    """<p>The target resources (e.g., SageMaker Training Jobs, SageMaker HyperPod, SageMaker Endpoints, Studio apps) for this training plan offering.</p> <p>Training plans are specific to their target resource.</p> <ul> <li> <p>A training plan designed for SageMaker training jobs can only be used to schedule and run training jobs.</p> </li> <li> <p>A training plan for HyperPod clusters can be used exclusively to provide compute resources to a cluster's instance group.</p> </li> <li> <p>A training plan for SageMaker endpoints can be used exclusively to provide compute resources to SageMaker endpoints for model deployment.</p> </li> <li> <p>A training plan for Studio apps can be used to launch JupyterLab and Code Editor apps on reserved training plan capacity.</p> </li> </ul>"""
    requested_start_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The requested start time that the user specified when searching for the training plan offering.</p>"""
    requested_end_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The requested end time that the user specified when searching for the training plan offering.</p>"""
    duration_hours: NotRequired[
        "capo_sagemaker.types.training_plan_duration_hours.TrainingPlanDurationHours"
    ]
    """<p>The number of whole hours in the total duration for this training plan offering.</p>"""
    duration_minutes: NotRequired[
        "capo_sagemaker.types.training_plan_duration_minutes.TrainingPlanDurationMinutes"
    ]
    """<p>The additional minutes beyond whole hours in the total duration for this training plan offering.</p>"""
    upfront_fee: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The upfront fee for this training plan offering.</p>"""
    currency_code: NotRequired["capo_sagemaker.types.currency_code.CurrencyCode"]
    """<p>The currency code for the upfront fee (e.g., USD).</p>"""
    reserved_capacity_offerings: NotRequired[
        "capo_sagemaker.types.reserved_capacity_offerings.ReservedCapacityOfferings"
    ]
    """<p>A list of reserved capacity offerings associated with this training plan offering.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanOffering) -> dict:
    out: dict = {}
    if "training_plan_offering_id" in value:
        out["TrainingPlanOfferingId"] = value["training_plan_offering_id"]
    if "target_resources" in value:
        import capo_sagemaker.types.sage_maker_resource_names

        out["TargetResources"] = (
            capo_sagemaker.types.sage_maker_resource_names.serialize_aws_json_1_1(
                value["target_resources"]
            )
        )
    if "requested_start_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["RequestedStartTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["requested_start_time_after"]
            )
        )
    if "requested_end_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["RequestedEndTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["requested_end_time_before"]
            )
        )
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "duration_minutes" in value:
        out["DurationMinutes"] = value["duration_minutes"]
    if "upfront_fee" in value:
        out["UpfrontFee"] = value["upfront_fee"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "reserved_capacity_offerings" in value:
        import capo_sagemaker.types.reserved_capacity_offerings

        out["ReservedCapacityOfferings"] = (
            capo_sagemaker.types.reserved_capacity_offerings.serialize_aws_json_1_1(
                value["reserved_capacity_offerings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingPlanOffering:
    out: TrainingPlanOffering = {}  # type: ignore[typeddict-item]
    if "TrainingPlanOfferingId" in data:
        out["training_plan_offering_id"] = data["TrainingPlanOfferingId"]
    if "TargetResources" in data:
        import capo_sagemaker.types.sage_maker_resource_names

        out["target_resources"] = (
            capo_sagemaker.types.sage_maker_resource_names.deserialize_aws_json_1_1(
                data["TargetResources"]
            )
        )
    if "RequestedStartTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["requested_start_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["RequestedStartTimeAfter"]
            )
        )
    if "RequestedEndTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["requested_end_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["RequestedEndTimeBefore"]
            )
        )
    if "DurationHours" in data:
        out["duration_hours"] = data["DurationHours"]
    if "DurationMinutes" in data:
        out["duration_minutes"] = data["DurationMinutes"]
    if "UpfrontFee" in data:
        out["upfront_fee"] = data["UpfrontFee"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "ReservedCapacityOfferings" in data:
        import capo_sagemaker.types.reserved_capacity_offerings

        out["reserved_capacity_offerings"] = (
            capo_sagemaker.types.reserved_capacity_offerings.deserialize_aws_json_1_1(
                data["ReservedCapacityOfferings"]
            )
        )
    return out
