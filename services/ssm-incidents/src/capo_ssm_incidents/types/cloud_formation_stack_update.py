"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CloudFormationStackUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn


class CloudFormationStackUpdate(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The timestamp for when the CloudFormation stack creation or update began.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the CloudFormation stack creation or update ended. Not reported for deployments that are still in progress.</p>"""
    stack_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the CloudFormation stack involved in the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationStackUpdate) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types._prelude.timestamp

    out["startTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        out["endTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    out["stackArn"] = value["stack_arn"]
    return out


def deserialize_json(data: dict) -> CloudFormationStackUpdate:
    out: CloudFormationStackUpdate = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import capo_ssm_incidents.types._prelude.timestamp

        out["start_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("CloudFormationStackUpdate.start_time required")
    if "endTime" in data:
        import capo_ssm_incidents.types._prelude.timestamp

        out["end_time"] = capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if "stackArn" in data:
        out["stack_arn"] = data["stackArn"]
    else:
        raise DeserializationError("CloudFormationStackUpdate.stack_arn required")
    return out
