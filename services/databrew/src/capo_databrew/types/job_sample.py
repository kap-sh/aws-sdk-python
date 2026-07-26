"""Generated from Smithy shape ``com.amazonaws.databrew#JobSample``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_size
    import capo_databrew.types.sample_mode


class JobSample(TypedDict, closed=True):
    mode: NotRequired["capo_databrew.types.sample_mode.SampleMode"]
    """<p>A value that determines whether the profile job is run on the entire dataset or a specified number of rows. This value must be one of the following:</p> <ul> <li> <p>FULL_DATASET - The profile job is run on the entire dataset.</p> </li> <li> <p>CUSTOM_ROWS - The profile job is run on the number of rows specified in the <code>Size</code> parameter.</p> </li> </ul>"""
    size: NotRequired["capo_databrew.types.job_size.JobSize"]
    """<p>The <code>Size</code> parameter is only required when the mode is CUSTOM_ROWS. The profile job is run on the specified number of rows. The maximum value for size is Long.MAX_VALUE.</p> <p>Long.MAX_VALUE = 9223372036854775807</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSample) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_databrew.types.sample_mode

        out["Mode"] = capo_databrew.types.sample_mode.serialize_json(value["mode"])
    if "size" in value:
        out["Size"] = value["size"]
    return out


def deserialize_json(data: dict) -> JobSample:
    out: JobSample = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import capo_databrew.types.sample_mode

        out["mode"] = capo_databrew.types.sample_mode.deserialize_json(data["Mode"])
    if "Size" in data:
        out["size"] = data["Size"]
    return out
