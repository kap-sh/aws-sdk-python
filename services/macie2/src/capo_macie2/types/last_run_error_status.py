"""Generated from Smithy shape ``com.amazonaws.macie2#LastRunErrorStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.last_run_error_status_code


class LastRunErrorStatus(TypedDict, closed=True):
    code: NotRequired[
        "capo_macie2.types.last_run_error_status_code.LastRunErrorStatusCode"
    ]
    """<p>Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run. Possible values are:</p> <ul><li><p>ERROR - One or more errors occurred. Amazon Macie didn't process all the data specified for the job.</p></li> <li><p>NONE - No errors occurred. Macie processed all the data specified for the job.</p></li></ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastRunErrorStatus) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_macie2.types.last_run_error_status_code

        out["code"] = capo_macie2.types.last_run_error_status_code.serialize_json(
            value["code"]
        )
    return out


def deserialize_json(data: dict) -> LastRunErrorStatus:
    out: LastRunErrorStatus = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import capo_macie2.types.last_run_error_status_code

        out["code"] = capo_macie2.types.last_run_error_status_code.deserialize_json(
            data["code"]
        )
    return out
