"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.reserved_instances_modification_result_list
    import aws_sdk_ec2.types.reserved_intances_ids
    import aws_sdk_ec2.types.string


class ReservedInstancesModification(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    create_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time when the modification request was created.</p>"""
    effective_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time for the modification to become effective.</p>"""
    modification_results: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_modification_result_list.ReservedInstancesModificationResultList"
    ]
    """<p>Contains target configurations along with their corresponding new Reserved Instance IDs.</p>"""
    reserved_instances_ids: NotRequired[
        "aws_sdk_ec2.types.reserved_intances_ids.ReservedIntancesIds"
    ]
    """<p>The IDs of one or more Reserved Instances.</p>"""
    reserved_instances_modification_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique ID for the Reserved Instance modification.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the Reserved Instances modification request.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the status.</p>"""
    update_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time when the modification request was last updated.</p>"""
