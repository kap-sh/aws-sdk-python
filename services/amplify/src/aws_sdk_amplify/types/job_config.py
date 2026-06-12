"""Generated from Smithy shape ``com.amazonaws.amplify#JobConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.build_compute_type


class JobConfig(TypedDict):
    build_compute_type: "aws_sdk_amplify.types.build_compute_type.BuildComputeType"
    """<p>Specifies the size of the build instance. Amplify supports three instance sizes: <code>STANDARD_8GB</code>, <code>LARGE_16GB</code>, and <code>XLARGE_72GB</code>. If you don't specify a value, Amplify uses the <code>STANDARD_8GB</code> default.</p> <p>The following list describes the CPU, memory, and storage capacity for each build instance type:</p> <dl> <dt>STANDARD_8GB</dt> <dd> <ul> <li> <p>vCPUs: 4</p> </li> <li> <p>Memory: 8 GiB</p> </li> <li> <p>Disk space: 128 GB</p> </li> </ul> </dd> <dt>LARGE_16GB</dt> <dd> <ul> <li> <p>vCPUs: 8</p> </li> <li> <p>Memory: 16 GiB</p> </li> <li> <p>Disk space: 128 GB</p> </li> </ul> </dd> <dt>XLARGE_72GB</dt> <dd> <ul> <li> <p>vCPUs: 36</p> </li> <li> <p>Memory: 72 GiB</p> </li> <li> <p>Disk space: 256 GB</p> </li> </ul> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobConfig) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.build_compute_type

    out["buildComputeType"] = aws_sdk_amplify.types.build_compute_type.serialize_json(
        value["build_compute_type"]
    )
    return out


def deserialize_json(data: dict) -> JobConfig:
    out: JobConfig = {}  # type: ignore[typeddict-item]
    if "buildComputeType" in data:
        import aws_sdk_amplify.types.build_compute_type

        out["build_compute_type"] = (
            aws_sdk_amplify.types.build_compute_type.deserialize_json(
                data["buildComputeType"]
            )
        )
    else:
        raise DeserializationError("JobConfig.build_compute_type required")
    return out
