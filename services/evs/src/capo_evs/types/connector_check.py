"""Generated from Smithy shape ``com.amazonaws.evs#ConnectorCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_evs.types.check_result
    import capo_evs.types.check_type


class ConnectorCheck(TypedDict, closed=True):
    type: NotRequired["capo_evs.types.check_type.CheckType"]
    """<p>The check type.</p>"""
    result: NotRequired["capo_evs.types.check_result.CheckResult"]
    """<p>The check result.</p>"""
    last_check_attempt: NotRequired["datetime.datetime"]
    """<p>The date and time of the last check attempt.</p>"""
    impaired_since: NotRequired["datetime.datetime"]
    """<p>The time when connector health began to be impaired.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectorCheck) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_evs.types.check_type

        out["type"] = capo_evs.types.check_type.serialize_aws_json_1_0(value["type"])
    if "result" in value:
        import capo_evs.types.check_result

        out["result"] = capo_evs.types.check_result.serialize_aws_json_1_0(
            value["result"]
        )
    if "last_check_attempt" in value:
        import capo_evs.types._prelude.timestamp

        out["lastCheckAttempt"] = (
            capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_check_attempt"]
            )
        )
    if "impaired_since" in value:
        import capo_evs.types._prelude.timestamp

        out["impairedSince"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["impaired_since"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectorCheck:
    out: ConnectorCheck = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_evs.types.check_type

        out["type"] = capo_evs.types.check_type.deserialize_aws_json_1_0(data["type"])
    if "result" in data:
        import capo_evs.types.check_result

        out["result"] = capo_evs.types.check_result.deserialize_aws_json_1_0(
            data["result"]
        )
    if "lastCheckAttempt" in data:
        import capo_evs.types._prelude.timestamp

        out["last_check_attempt"] = (
            capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastCheckAttempt"]
            )
        )
    if "impairedSince" in data:
        import capo_evs.types._prelude.timestamp

        out["impaired_since"] = (
            capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["impairedSince"]
            )
        )
    return out
