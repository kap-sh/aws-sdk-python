"""Generated from Smithy shape ``com.amazonaws.mturk#Qualification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.customer_id
    import capo_mturk.types.entity_id
    import capo_mturk.types.integer
    import capo_mturk.types.locale
    import capo_mturk.types.qualification_status
    import capo_mturk.types.timestamp


class Qualification(TypedDict, closed=True):
    qualification_type_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> The ID of the Qualification type for the Qualification.</p>"""
    worker_id: NotRequired["capo_mturk.types.customer_id.CustomerId"]
    """<p> The ID of the Worker who possesses the Qualification. </p>"""
    grant_time: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> The date and time the Qualification was granted to the Worker. If the Worker's Qualification was revoked, and then re-granted based on a new Qualification request, GrantTime is the date and time of the last call to the AcceptQualificationRequest operation.</p>"""
    integer_value: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The value (score) of the Qualification, if the Qualification has an integer value.</p>"""
    locale_value: NotRequired["capo_mturk.types.locale.Locale"]
    status: NotRequired["capo_mturk.types.qualification_status.QualificationStatus"]
    """<p> The status of the Qualification. Valid values are Granted | Revoked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Qualification) -> dict:
    out: dict = {}
    if "qualification_type_id" in value:
        out["QualificationTypeId"] = value["qualification_type_id"]
    if "worker_id" in value:
        out["WorkerId"] = value["worker_id"]
    if "grant_time" in value:
        import capo_mturk.types.timestamp

        out["GrantTime"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["grant_time"]
        )
    if "integer_value" in value:
        out["IntegerValue"] = value["integer_value"]
    if "locale_value" in value:
        import capo_mturk.types.locale

        out["LocaleValue"] = capo_mturk.types.locale.serialize_aws_json_1_1(
            value["locale_value"]
        )
    if "status" in value:
        import capo_mturk.types.qualification_status

        out["Status"] = capo_mturk.types.qualification_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Qualification:
    out: Qualification = {}  # type: ignore[typeddict-item]
    if "QualificationTypeId" in data:
        out["qualification_type_id"] = data["QualificationTypeId"]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    if "GrantTime" in data:
        import capo_mturk.types.timestamp

        out["grant_time"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["GrantTime"]
        )
    if "IntegerValue" in data:
        out["integer_value"] = data["IntegerValue"]
    if "LocaleValue" in data:
        import capo_mturk.types.locale

        out["locale_value"] = capo_mturk.types.locale.deserialize_aws_json_1_1(
            data["LocaleValue"]
        )
    if "Status" in data:
        import capo_mturk.types.qualification_status

        out["status"] = capo_mturk.types.qualification_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
