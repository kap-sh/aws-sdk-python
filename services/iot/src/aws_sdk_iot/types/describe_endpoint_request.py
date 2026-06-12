"""Generated from Smithy shape ``com.amazonaws.iot#DescribeEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.endpoint_type


class DescribeEndpointRequest(TypedDict):
    endpoint_type: NotRequired["aws_sdk_iot.types.endpoint_type.EndpointType"]
    """<p>The endpoint type. Valid endpoint types include:</p> <ul> <li> <p> <code>iot:Data</code> - Returns a VeriSign signed data endpoint.</p> </li> </ul> <ul> <li> <p> <code>iot:Data-ATS</code> - Returns an ATS signed data endpoint.</p> </li> </ul> <ul> <li> <p> <code>iot:CredentialProvider</code> - Returns an IoT credentials provider API endpoint.</p> </li> </ul> <ul> <li> <p> <code>iot:Jobs</code> - Returns an IoT device management Jobs API endpoint.</p> </li> </ul> <p>We strongly recommend that customers use the newer <code>iot:Data-ATS</code> endpoint type to avoid issues related to the widespread distrust of Symantec certificate authorities. ATS Signed Certificates are more secure and are trusted by most popular browsers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEndpointRequest:
    out: DescribeEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
