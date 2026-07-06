"""Generated from Smithy shape ``com.amazonaws.connect#AssociateHoursOfOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.parent_hours_of_operation_config_list


class AssociateHoursOfOperationsRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    hours_of_operation_id: (
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    )
    """<p>The identifier of the child hours of operation.</p>"""
    parent_hours_of_operation_configs: "aws_sdk_connect.types.parent_hours_of_operation_config_list.ParentHoursOfOperationConfigList"
    """<p>The Amazon Resource Names (ARNs) of the parent hours of operation resources to associate with the child hours of operation resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateHoursOfOperationsRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.parent_hours_of_operation_config_list

    out["ParentHoursOfOperationConfigs"] = (
        aws_sdk_connect.types.parent_hours_of_operation_config_list.serialize_json(
            value["parent_hours_of_operation_configs"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateHoursOfOperationsRequest:
    out: AssociateHoursOfOperationsRequest = {}  # type: ignore[typeddict-item]
    if "ParentHoursOfOperationConfigs" in data:
        import aws_sdk_connect.types.parent_hours_of_operation_config_list

        out["parent_hours_of_operation_configs"] = (
            aws_sdk_connect.types.parent_hours_of_operation_config_list.deserialize_json(
                data["ParentHoursOfOperationConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateHoursOfOperationsRequest.parent_hours_of_operation_configs required"
        )
    return out
