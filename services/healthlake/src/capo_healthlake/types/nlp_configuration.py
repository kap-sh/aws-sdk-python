"""Generated from Smithy shape ``com.amazonaws.healthlake#NlpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.nlp_status


class NlpConfiguration(TypedDict, closed=True):
    status: NotRequired["capo_healthlake.types.nlp_status.NlpStatus"]
    """<para>The status of the NLP configuration.</para>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NlpConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_healthlake.types.nlp_status

        out["Status"] = capo_healthlake.types.nlp_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NlpConfiguration:
    out: NlpConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_healthlake.types.nlp_status

        out["status"] = capo_healthlake.types.nlp_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out
