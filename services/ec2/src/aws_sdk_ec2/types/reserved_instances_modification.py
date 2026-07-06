"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.reserved_instances_modification_result_list
    import aws_sdk_ec2.types.reserved_intances_ids
    import aws_sdk_ec2.types.string


class ReservedInstancesModification(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesModification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "create_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "effective_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["effective_date"], pairs, f"{prefix}.EffectiveDate"
        )
    if "modification_results" in value:
        import aws_sdk_ec2.types.reserved_instances_modification_result_list

        aws_sdk_ec2.types.reserved_instances_modification_result_list.serialize_ec2_query(
            value["modification_results"], pairs, f"{prefix}.ModificationResultSet"
        )
    if "reserved_instances_ids" in value:
        import aws_sdk_ec2.types.reserved_intances_ids

        aws_sdk_ec2.types.reserved_intances_ids.serialize_ec2_query(
            value["reserved_instances_ids"], pairs, f"{prefix}.ReservedInstancesSet"
        )
    if "reserved_instances_modification_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedInstancesModificationId",
                str(value["reserved_instances_modification_id"]),
            )
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "update_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["update_date"], pairs, f"{prefix}.UpdateDate"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesModification:
    out: ReservedInstancesModification = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_ec2.types.date_time

        out["create_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_create_date
        )
    child_effective_date = el.find("EffectiveDate")
    if child_effective_date is not None:
        import aws_sdk_ec2.types.date_time

        out["effective_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_effective_date
        )
    if el.find("ModificationResultSet") is not None:
        import aws_sdk_ec2.types.reserved_instances_modification_result_list

        out["modification_results"] = (
            aws_sdk_ec2.types.reserved_instances_modification_result_list.deserialize_ec2_query(
                el, "ModificationResultSet"
            )
        )
    if el.find("ReservedInstancesSet") is not None:
        import aws_sdk_ec2.types.reserved_intances_ids

        out["reserved_instances_ids"] = (
            aws_sdk_ec2.types.reserved_intances_ids.deserialize_ec2_query(
                el, "ReservedInstancesSet"
            )
        )
    child_reserved_instances_modification_id = el.find(
        "ReservedInstancesModificationId"
    )
    if child_reserved_instances_modification_id is not None:
        out["reserved_instances_modification_id"] = str(
            child_reserved_instances_modification_id.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_update_date = el.find("UpdateDate")
    if child_update_date is not None:
        import aws_sdk_ec2.types.date_time

        out["update_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_update_date
        )
    return out
