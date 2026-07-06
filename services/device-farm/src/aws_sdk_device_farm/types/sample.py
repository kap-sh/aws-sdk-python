"""Generated from Smithy shape ``com.amazonaws.devicefarm#Sample``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.sample_type
    import aws_sdk_device_farm.types.url


class Sample(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The sample's ARN.</p>"""
    type: NotRequired["aws_sdk_device_farm.types.sample_type.SampleType"]
    """<p>The sample's type.</p> <p>Must be one of the following values:</p> <ul> <li> <p>CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage.</p> </li> <li> <p>MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes.</p> </li> <li> <p>NATIVE_AVG_DRAWTIME</p> </li> <li> <p>NATIVE_FPS</p> </li> <li> <p>NATIVE_FRAMES</p> </li> <li> <p>NATIVE_MAX_DRAWTIME</p> </li> <li> <p>NATIVE_MIN_DRAWTIME</p> </li> <li> <p>OPENGL_AVG_DRAWTIME</p> </li> <li> <p>OPENGL_FPS</p> </li> <li> <p>OPENGL_FRAMES</p> </li> <li> <p>OPENGL_MAX_DRAWTIME</p> </li> <li> <p>OPENGL_MIN_DRAWTIME</p> </li> <li> <p>RX</p> </li> <li> <p>RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process.</p> </li> <li> <p>THREADS: A threads sample type. This is expressed as the total number of threads per app process.</p> </li> <li> <p>TX</p> </li> <li> <p>TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process.</p> </li> </ul>"""
    url: NotRequired["aws_sdk_device_farm.types.url.URL"]
    """<p>The presigned Amazon S3 URL that can be used with a GET request to download the sample's file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sample) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import aws_sdk_device_farm.types.sample_type

        out["type"] = aws_sdk_device_farm.types.sample_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Sample:
    out: Sample = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        import aws_sdk_device_farm.types.sample_type

        out["type"] = aws_sdk_device_farm.types.sample_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "url" in data:
        out["url"] = data["url"]
    return out
