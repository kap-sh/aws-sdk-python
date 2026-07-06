"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateRelatedItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.client_token
    import aws_sdk_ssm_incidents.types.related_items_update


class UpdateRelatedItemsInput(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that a client calls the operation only once with the specified details.</p>"""
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record that contains the related items that you update.</p>"""
    related_items_update: (
        "aws_sdk_ssm_incidents.types.related_items_update.RelatedItemsUpdate"
    )
    """<p>Details about the item that you are add to, or delete from, an incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRelatedItemsInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["incidentRecordArn"] = value["incident_record_arn"]
    import aws_sdk_ssm_incidents.types.related_items_update

    out["relatedItemsUpdate"] = (
        aws_sdk_ssm_incidents.types.related_items_update.serialize_json(
            value["related_items_update"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRelatedItemsInput:
    out: UpdateRelatedItemsInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError(
            "UpdateRelatedItemsInput.incident_record_arn required"
        )
    if "relatedItemsUpdate" in data:
        import aws_sdk_ssm_incidents.types.related_items_update

        out["related_items_update"] = (
            aws_sdk_ssm_incidents.types.related_items_update.deserialize_json(
                data["relatedItemsUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRelatedItemsInput.related_items_update required"
        )
    return out
