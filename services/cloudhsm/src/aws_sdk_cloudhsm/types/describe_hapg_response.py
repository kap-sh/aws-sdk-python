"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DescribeHapgResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.cloud_hsm_object_state
    import aws_sdk_cloudhsm.types.hapg_arn
    import aws_sdk_cloudhsm.types.hsm_list
    import aws_sdk_cloudhsm.types.label
    import aws_sdk_cloudhsm.types.partition_serial_list
    import aws_sdk_cloudhsm.types.string
    import aws_sdk_cloudhsm.types.timestamp


class DescribeHapgResponse(TypedDict, closed=True):
    hapg_arn: NotRequired["aws_sdk_cloudhsm.types.hapg_arn.HapgArn"]
    """<p>The ARN of the high-availability partition group.</p>"""
    hapg_serial: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The serial number of the high-availability partition group.</p>"""
    hsms_last_action_failed: NotRequired["aws_sdk_cloudhsm.types.hsm_list.HsmList"]
    """<p></p>"""
    hsms_pending_deletion: NotRequired["aws_sdk_cloudhsm.types.hsm_list.HsmList"]
    """<p></p>"""
    hsms_pending_registration: NotRequired["aws_sdk_cloudhsm.types.hsm_list.HsmList"]
    """<p></p>"""
    label: NotRequired["aws_sdk_cloudhsm.types.label.Label"]
    """<p>The label for the high-availability partition group.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_cloudhsm.types.timestamp.Timestamp"]
    """<p>The date and time the high-availability partition group was last modified.</p>"""
    partition_serial_list: NotRequired[
        "aws_sdk_cloudhsm.types.partition_serial_list.PartitionSerialList"
    ]
    """<p>The list of partition serial numbers that belong to the high-availability partition group.</p>"""
    state: NotRequired[
        "aws_sdk_cloudhsm.types.cloud_hsm_object_state.CloudHsmObjectState"
    ]
    """<p>The state of the high-availability partition group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHapgResponse) -> dict:
    out: dict = {}
    if "hapg_arn" in value:
        out["HapgArn"] = value["hapg_arn"]
    if "hapg_serial" in value:
        out["HapgSerial"] = value["hapg_serial"]
    if "hsms_last_action_failed" in value:
        import aws_sdk_cloudhsm.types.hsm_list

        out["HsmsLastActionFailed"] = (
            aws_sdk_cloudhsm.types.hsm_list.serialize_aws_json_1_1(
                value["hsms_last_action_failed"]
            )
        )
    if "hsms_pending_deletion" in value:
        import aws_sdk_cloudhsm.types.hsm_list

        out["HsmsPendingDeletion"] = (
            aws_sdk_cloudhsm.types.hsm_list.serialize_aws_json_1_1(
                value["hsms_pending_deletion"]
            )
        )
    if "hsms_pending_registration" in value:
        import aws_sdk_cloudhsm.types.hsm_list

        out["HsmsPendingRegistration"] = (
            aws_sdk_cloudhsm.types.hsm_list.serialize_aws_json_1_1(
                value["hsms_pending_registration"]
            )
        )
    if "label" in value:
        out["Label"] = value["label"]
    if "last_modified_timestamp" in value:
        out["LastModifiedTimestamp"] = value["last_modified_timestamp"]
    if "partition_serial_list" in value:
        import aws_sdk_cloudhsm.types.partition_serial_list

        out["PartitionSerialList"] = (
            aws_sdk_cloudhsm.types.partition_serial_list.serialize_aws_json_1_1(
                value["partition_serial_list"]
            )
        )
    if "state" in value:
        import aws_sdk_cloudhsm.types.cloud_hsm_object_state

        out["State"] = (
            aws_sdk_cloudhsm.types.cloud_hsm_object_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHapgResponse:
    out: DescribeHapgResponse = {}  # type: ignore[typeddict-item]
    if "HapgArn" in data:
        out["hapg_arn"] = data["HapgArn"]
    if "HapgSerial" in data:
        out["hapg_serial"] = data["HapgSerial"]
    if "HsmsLastActionFailed" in data:
        import aws_sdk_cloudhsm.types.hsm_list

        out["hsms_last_action_failed"] = (
            aws_sdk_cloudhsm.types.hsm_list.deserialize_aws_json_1_1(
                data["HsmsLastActionFailed"]
            )
        )
    if "HsmsPendingDeletion" in data:
        import aws_sdk_cloudhsm.types.hsm_list

        out["hsms_pending_deletion"] = (
            aws_sdk_cloudhsm.types.hsm_list.deserialize_aws_json_1_1(
                data["HsmsPendingDeletion"]
            )
        )
    if "HsmsPendingRegistration" in data:
        import aws_sdk_cloudhsm.types.hsm_list

        out["hsms_pending_registration"] = (
            aws_sdk_cloudhsm.types.hsm_list.deserialize_aws_json_1_1(
                data["HsmsPendingRegistration"]
            )
        )
    if "Label" in data:
        out["label"] = data["Label"]
    if "LastModifiedTimestamp" in data:
        out["last_modified_timestamp"] = data["LastModifiedTimestamp"]
    if "PartitionSerialList" in data:
        import aws_sdk_cloudhsm.types.partition_serial_list

        out["partition_serial_list"] = (
            aws_sdk_cloudhsm.types.partition_serial_list.deserialize_aws_json_1_1(
                data["PartitionSerialList"]
            )
        )
    if "State" in data:
        import aws_sdk_cloudhsm.types.cloud_hsm_object_state

        out["state"] = (
            aws_sdk_cloudhsm.types.cloud_hsm_object_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
